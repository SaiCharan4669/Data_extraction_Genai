# Create Gradio interface
import gradio as gr
with gr.Blocks() as app:
    gr.Markdown("##  Data Extraction from invoices and handwritten files")
    gr.Markdown("Upload a receipt image and provide a custom prompt for extracting information.")

    with gr.Row():
        image_input = gr.Image(label="Upload Receipt Image", type="pil")
        user_prompt_input = gr.Textbox(label="User Prompt", placeholder="E.g., 'Convert invoice data to JSON format'")

    output_display = gr.Textbox(label="Output")

    # Create a button to trigger the processing function
    submit_button = gr.Button("Process Receipt")

    # Set up event handling
    submit_button.click(fn=process_receipt,
                        inputs=[image_input, user_prompt_input],
                        outputs=output_display)

# Launch the app
app.launch(share=True)
