import logging
import queue
import threading
import time
import gradio as gr
from deal_agent_framework import DealAgentFramework
from agents.deals import Opportunity, Deal
from log_utils import reformat
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

class QueueHandler(logging.Handler):
    def __init__(self, log_queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.put(self.format(record))

def html_for(log_data):
    output = '<br>'.join(log_data[-18:])
    return f"""
    <div id="scrollContent" style="height: 400px; overflow-y: auto; border: 1px solid #ccc; background-color: #222229; padding: 10px;">
    {output}
    </div>
    """

def setup_logging(log_queue):
    handler = QueueHandler(log_queue)
    formatter = logging.Formatter(
        "[%(asctime)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S %z",
    )
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
                

class App:

    def __init__(self):    
        self.agent_framework = None

    def get_agent_framework(self):
        if not self.agent_framework:
            self.agent_framework = DealAgentFramework()
            self.agent_framework.init_agents_as_needed()
        return self.agent_framework

    def run(self):
        with gr.Blocks(title="The Price is Right", fill_width=True) as ui:
            
            log_data = gr.State([])
            
            def table_for(opps):
                return [[opp.deal.product_description, f"${opp.deal.price:.2f}", f"${opp.estimate:.2f}", f"${opp.discount:.2f}", opp.deal.url] for opp in opps]

            def update_output(log_data, log_queue, result_queue):
                initial_result = table_for(self.get_agent_framework().memory)
                final_result = None
                while True:
                    try:
                        message = log_queue.get_nowait()
                        log_data.append(reformat(message))
                        yield log_data, html_for(log_data), final_result or initial_result
                    except queue.Empty:
                        try:
                            final_result = result_queue.get_nowait()
                            yield log_data, html_for(log_data), final_result or initial_result
                        except queue.Empty:
                            if final_result is not None:
                                break
                            time.sleep(0.1)

            def get_initial_plot():
                fig = go.Figure()
                fig.update_layout(
                    title='Loading vector DB...',
                    height=400,
                )
                return fig

            def get_plot():
                documents, vectors, prices, price_bins, hover_texts = DealAgentFramework.get_plot_data(max_datapoints=1000)
                # Create the 3D scatter plot
                df = pd.DataFrame({
                    'x': vectors[:, 0],
                    'y': vectors[:, 1],
                    'z': vectors[:, 2],
                    'Price': prices,
                    'Price_Bin': price_bins,
                    'hover_text': hover_texts
                })
                
               
                fig = px.scatter_3d(
                    df,
                    x='x',
                    y='y',
                    z='z',
                    color='Price_Bin',
                    hover_name='hover_text',
                    symbol='Price_Bin',
                    size_max=12,
                    title='3D Chroma Vectorstore Visualization by Price Range',
                    labels={'x': 'TSNE-1', 'y': 'TSNE-2', 'z': 'TSNE-3'},
                    height=400,
                )
                
                # Customize markers and layout
                fig.update_traces(marker=dict(size=6, opacity=0.75))
                fig.update_layout(
                    legend_title_text='Price Range',
                    font=dict(size=12),
                    margin=dict(r=20, b=10, l=10, t=40),
                    scene=dict(
                        xaxis_title='x',
                        yaxis_title='y',
                        zaxis_title='z',
                        bgcolor='white'
                    )
                )

                return fig
        
            def do_run():
                new_opportunities = self.get_agent_framework().run()
                table = table_for(new_opportunities)
                return table

            def run_with_logging(initial_log_data):
                log_queue = queue.Queue()
                result_queue = queue.Queue()
                setup_logging(log_queue)
                
                def worker():
                    result = do_run()
                    result_queue.put(result)
                
                thread = threading.Thread(target=worker)
                thread.start()
                
                for log_data, output, final_result in update_output(initial_log_data, log_queue, result_queue):
                    yield log_data, output, final_result

            def do_select(selected_index: gr.SelectData):
                opportunities = self.get_agent_framework().memory
                row = selected_index.index[0]
                opportunity = opportunities[row]
                self.get_agent_framework().planner.messenger.alert(opportunity)
        
            with gr.Row():
                gr.Markdown('<div style="text-align: center;font-size:24px"><strong>The Price is Right</strong> - Autonomous Agent Framework that hunts for deals</div>')
            with gr.Row():
                gr.Markdown('<div style="text-align: center;font-size:14px">A proprietary RAG pipeline with a frontier model collaborate to send push notifications with great online deals.</div>')
            with gr.Row():
                opportunities_dataframe = gr.Dataframe(
                    headers=["Deals found so far", "Price", "Estimate", "Discount", "URL"],
                    wrap=True,
                    column_widths=[6, 1, 1, 1, 3],
                    row_count=10,
                    col_count=5,
                    max_height=400,
                )
            with gr.Row():
                with gr.Column(scale=1):
                    logs = gr.HTML()
                with gr.Column(scale=1):
                    plot = gr.Plot(value=get_plot(), show_label=False)
        
            ui.load(run_with_logging, inputs=[log_data], outputs=[log_data, logs, opportunities_dataframe])

            timer = gr.Timer(value=300, active=True)
            timer.tick(run_with_logging, inputs=[log_data], outputs=[log_data, logs, opportunities_dataframe])

            opportunities_dataframe.select(do_select)
        
        ui.launch(share=False, inbrowser=True)

if __name__=="__main__":
    App().run()
    


