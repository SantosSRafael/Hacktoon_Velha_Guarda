from app.gravacao_de_audio import Gravador

def create_app():
  gravador = Gravador(
    block_size=1024,
    sample_rate=44100,
    channels=1,
    output_file_name='output.wav',
    input_file_name='input.wav',
    final_path_audio='C:/Users/user/Documents/', ## Colocar aqui o caminho em que o arquivo deve cair
    cOperador=1,
    cCliente=1
  )

  gravador.gravar()   