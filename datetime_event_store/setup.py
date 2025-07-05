from setuptools import setup, find_packages
#il faut au prealable installer les packages setuptools, requests et Flask
setup(
    name="datetime_event_store",
    description="Un package pour stocker et récupérer des événements associés à des datetime.",
    author="Abdel Majid Boukhlik",
    packages=find_packages(),
)