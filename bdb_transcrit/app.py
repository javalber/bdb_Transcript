import gradio as gr
import tempfile
from whisper_utils import transcribe_audio

def handle_upload(file):
    # Guardar archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name

    # Transcribir
    result = transcribe_audio(tmp_path)
    return result["text"]

# Interfaz Gradio
interface = gr.Interface(
    fn=handle_upload,
    inputs=gr.Audio(source="upload", type="file"),
    outputs="text",
    title="Transcriptor de Audio",
    description="Sube un archivo .mp3 o .mp4 para obtener la transcripción."
)

if __name__ == "__main__":
    interface.launch()
