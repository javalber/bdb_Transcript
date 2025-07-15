import gradio as gr
import os
from whisper_utils import transcribe_audio
from export_utils import export_to_docx, export_to_csv

def handle_upload(file):
    file_path = file  # Gradio File component ya proporciona la ruta
    result = transcribe_audio(file_path)
    return result['text'], result['segments']

def download_docx(text):
    path = export_to_docx(text)
    return path

def download_csv(segments):
    path = export_to_csv(segments)
    return path

with gr.Blocks() as interface:
    gr.Markdown("## 🎙️ Transcript App - Suba su audio MP3 o MP4")

    with gr.Row():
        audio_input = gr.File(label="Archivo .mp3 o .mp4", file_types=[".mp3", ".mp4"])
        transcribe_btn = gr.Button("Transcribir")

    with gr.Row():
        full_text_output = gr.Textbox(label="Transcripción Completa", lines=10)

    segments_output = gr.JSON(label="Segmentos por fragmento")

    with gr.Row():
        docx_btn = gr.Button("📄 Exportar a Word")
        csv_btn = gr.Button("🧾 Exportar a CSV")

    docx_file = gr.File(label="Descarga Word")
    csv_file = gr.File(label="Descarga CSV")

    transcribe_btn.click(fn=handle_upload, inputs=[audio_input], outputs=[full_text_output, segments_output])
    docx_btn.click(fn=download_docx, inputs=[full_text_output], outputs=[docx_file])
    csv_btn.click(fn=download_csv, inputs=[segments_output], outputs=[csv_file])

if __name__ == "__main__":
    interface.launch()
    