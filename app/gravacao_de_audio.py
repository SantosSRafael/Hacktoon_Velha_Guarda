import speech_recognition as sr
import soundcard as sc
import soundfile as sf

class Gravador:
    def __init__(self, nome):
        self.nome = nome

    def saudacao(self):
        print(f"Olá, {self.nome}!")

def funcao_a():    

    # Obter o dispositivo de saída de áudio padrão
    output_device = sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True)

    # Configurar a taxa de amostragem e o número de canais
    sample_rate = 44100
    channels = 2
    output_file_name = 'output.wav'

    # Configurar o buffer de gravação
    block_size = 1024

    # # Criar o gravador de áudio
    # recorder = output_device.recorder(samplerate=sample_rate, channels=channels)        

    # Abrir o arquivo de destino para gravação
    output_file = sf.SoundFile(output_file_name, mode='w', samplerate=sample_rate, channels=channels)

    with output_device.recorder(samplerate=sample_rate, channels=channels) as recorder:
        try:
            # Loop de gravação em tempo real
            while True:
                # Ler o áudio do buffer
                data = recorder.record(block_size)

                # Gravar os dados no arquivo de destino
                output_file.write(data)

        except KeyboardInterrupt:
            print("Gravação interrompida pelo usuário.")

    # Fechar o arquivo de destino
    output_file.close()

    # try:
    #     print('Processando...')
    #     # Realizar o reconhecimento de fala a partir do arquivo WAV
    #     with sr.AudioFile(output_file_name) as source:
    #         audio_data = r.record(source)        
    #         text = r.recognize_google(audio_data, language="pt-BR")
    #         print("Texto transcrito:", text)
                                                    
    # except sr.UnknownValueError:
    #     print("Não foi possível transcrever o áudio.")
    # except sr.RequestError as e:
    #     print("Erro na requisição ao PocketSphinx; {0}".format(e))
