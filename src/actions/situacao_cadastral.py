from src.config.browser import open_browser

def consultar_situacao(playwright, cpf):

    # definir entradas
    url = "https://www.situacao-cadastral.com/"
    input_selector = "input[placeholder='CPF ou CNPJ']"
    submit_button = "input[title='Clique para consultar!']"

    try:
        #instanciar navegador
        browser = open_browser(playwright)
        page = browser.new_page()

        # abrir navegador e aguardar pelo carregamento.
        page.goto(url)
        page.wait_for_selector(input_selector)

        # digitar o cpf
        page.type(input_selector, cpf)

        # clicar para consultar.
        page.click(submit_button)

        # aguardar carregamento
        page.wait_for_selector(".dados.nome", timeout=15000)

        # obter dados da consulta
        dados_consulta = page.locator("#resultado").inner_text()
        return dados_consulta
    except Exception as e:
        return  f"Falha ao realizar consulta cadastral: {e.args}"
