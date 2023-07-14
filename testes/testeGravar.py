import soundcard as sc
import soundfile as sf

import juntaAudios as ja

output_device = sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True)
input_device = sc.get_microphone(id=str(sc.default_microphone().name), include_loopback=True)

if output_device is None:
    print("Nenhum dispositivo de saída encontrado.")
    exit()

if input_device is None:
    print("Nenhum dispositivo de entrada encontrado.")
    exit()

# Configurar o buffer de gravação
block_size = 1024
sample_rate = 44100
channels = 1
output_file_name = 'output.wav'
input_file_name = 'input.wav'

output_file = sf.SoundFile(output_file_name, mode='w', samplerate=sample_rate, channels=channels)
input_file = sf.SoundFile(input_file_name, mode='w', samplerate=sample_rate, channels=channels)


with output_device.recorder(samplerate=sample_rate, channels=channels) as pc_recorder, \
        input_device.recorder(samplerate=sample_rate, channels=channels) as mic_recorder:
    
    try:

        print('#' * 80)
        print('press Ctrl+C to stop the recording')
        print('#' * 80)
        # Loop de gravação em tempo real
        while True:
            # Ler o áudio do buffer
            data = pc_recorder.record(block_size)
            data2 = mic_recorder.record(block_size)
            # # Gravar os dados no arquivo de destino
            output_file.write(data)  
            input_file.write(data2)              

    except KeyboardInterrupt:
        print("Gravação interrompida pelo usuário.")          

# with recorder as recorder:
#       try:
#           # Loop de gravação em tempo real
#           while True:
#               # Ler o áudio do buffer
#               data = recorder.record(block_size)              
#               # Gravar os dados no arquivo de destino
#               output_file.write(data)  # Defina a taxa de amostragem correspondente

#       except KeyboardInterrupt:
#           print("Gravação interrompida pelo usuário.")    

# Salve os áudios
output_file.close()
input_file.close()

ja.unifica_audio('output.wav', 'input.wav')