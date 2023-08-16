import soundcard as sc
import soundfile as sf
import app.junta_audios as ja


class Gravador:
    def __init__(self, block_size, sample_rate, channels , output_file_name, input_file_name, final_path_audio, cOperador, cCliente):
        self.block_size = block_size #1024
        self.sample_rate = sample_rate #44100
        self.channels = channels #1
        self.output_file_name = output_file_name #'output.wav'
        self.input_file_name = input_file_name #'input.wav'
        self.final_path_audio = final_path_audio 
        self.cOperador = cOperador
        self.cCliente = cCliente

    def gravar(self):        
        output_device = sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True)
        input_device = sc.get_microphone(id=str(sc.default_microphone().name), include_loopback=True)

        if output_device is None:
            print("Nenhum dispositivo de saída encontrado.")
            exit()

        if input_device is None:
            print("Nenhum dispositivo de entrada encontrado.")
            exit()

        print(input_device, output_device)

        # Configurar o buffer de gravação


        output_file = sf.SoundFile(self.output_file_name, mode='w', samplerate=self.sample_rate, channels=self.channels)
        input_file = sf.SoundFile(self.input_file_name, mode='w', samplerate=self.sample_rate, channels=self.channels)


        with output_device.recorder(samplerate=self.sample_rate, channels=self.channels) as pc_recorder, \
                input_device.recorder(samplerate=self.sample_rate, channels=self.channels) as mic_recorder:
            
            try:

                print('#' * 80)
                print('Pressione Ctrl+C para parar de gravar')
                print('#' * 80)
                # Loop de gravação em tempo real
                while True:
                    # Ler o áudio do buffer
                    data = pc_recorder.record(self.block_size)
                    data2 = mic_recorder.record(self.block_size)
                    # # Gravar os dados no arquivo de destino
                    output_file.write(data)  
                    input_file.write(data2)              

            except KeyboardInterrupt:
                print("Gravação interrompida pelo usuário.")          

        # Salve os áudios
        output_file.close()
        input_file.close()

        print("Gravação finalizada. Gerando áudio unificado...")
        ja.unifica_audio(self.output_file_name, self.input_file_name, self.final_path_audio, self.cOperador, self.cCliente)
