import soundcard as sc
import soundfile as sf

output_device = sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True)

if output_device is None:
    print("Nenhum dispositivo de saída encontrado.")
    exit()

# Configurar o buffer de gravação
block_size = 1024
sample_rate = 44100
channels = 2
output_file_name = 'output.wav'

clear_chunks = []

for i in range(1024):
  clear_chunks.append(0)

# Abra um gravador de áudio para o dispositivo de saída selecionado
recorder = output_device.recorder(samplerate=sample_rate, channels=channels)  # Defina a taxa de amostragem desejada   
output_file = sf.SoundFile(output_file_name, mode='w', samplerate=sample_rate, channels=channels)
# Grava o áudio do lado esquerdo em formato mono
with recorder as recorder:
      try:
          # Loop de gravação em tempo real
          while True:
              # Ler o áudio do buffer
              data = recorder.record(block_size)
              #Remove os dados do lado esquerdo
              data[:, 0] = clear_chunks
              # left_channel = data
              # print(left_channel)              
              # Gravar os dados no arquivo de destino
              output_file.write(data)  # Defina a taxa de amostragem correspondente

      except KeyboardInterrupt:
          print("Gravação interrompida pelo usuário.")

# Salve o áudio do lado esquerdo em um arquivo WAV


# Encerre o gravador
output_file.close()