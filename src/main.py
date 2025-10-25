from playwright.sync_api import sync_playwright
from src.actions.situacao_cadastral import consultar_situacao
import logging


logging.basicConfig(
    filename="consulta-cadastral-log",
    level=logging.INFO
)

with sync_playwright() as playwright:
    logging.info("realizando consulta cadastral.")
    resultado = consultar_situacao(playwright, "47983653867")
    logging.info(f"resultado da consulta: {resultado}")

