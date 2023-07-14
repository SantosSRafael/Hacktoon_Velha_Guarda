import soundfile as sf
import numpy as np

def unifica_audio(audio_esquerda_path, audio_direita_path):

  # Defina o caminho para os dois arquivos de áudio que você deseja combinar
  # audio_esquerda_path = 'caminho_para_o_audio_esquerda.wav'
  # audio_direita_path = 'caminho_para_o_audio_direita.wav'

  # Carregue os arquivos de áudio usando a função `read` do soundfile
  audio_esquerda, samplerate_esquerda = sf.read(audio_esquerda_path)
  audio_direita, samplerate_direita = sf.read(audio_direita_path)

  print(audio_esquerda, audio_direita)

  # Verifique se as taxas de amostragem dos dois arquivos são iguais
  if samplerate_esquerda != samplerate_direita:
      print('As taxas de amostragem dos arquivos de áudio são diferentes. Não é possível combinar.')
      exit()

  # Verifique se o número de canais dos dois arquivos é igual a 1
  if audio_esquerda.ndim != 1 or audio_direita.ndim != 1:
      print('Os arquivos de áudio não têm um único canal. Não é possível combinar.')
      exit()

  # Crie um novo array numpy para o áudio combinado com dois canais
  audio_combinado = np.column_stack((audio_esquerda, audio_direita))

  # Defina o caminho para o arquivo de saída combinado
  audio_combinado_path = 'caminho_para_o_audio_combinado.wav'

  # Salve o áudio combinado no arquivo de saída usando a função `write` do soundfile
  sf.write(audio_combinado_path, audio_combinado, samplerate_esquerda, subtype='PCM_16')

  print('Áudio combinado salvo com sucesso.')

# unifica_audio('output.wav', 'input.wav')