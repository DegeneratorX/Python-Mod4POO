class LogMixin:
    @staticmethod  # Por não precisar de self, o melhor é tratar esse método como estático para evitar comportamentos estranhos.
    def write(msg):
        with open('log.log', 'a+') as f:  # a+ escreve sempre colocando na última linha dados
            f.write(msg)  # Erro
            f.write('\n')  # Pulo de linha

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')
