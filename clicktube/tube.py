import click
from pytube import YouTube

@click.group('cli')
def cli():
    pass


@cli.command()
@click.argument('link',type=click.STRING)
def audio(link):
    yt = YouTube(link).streams.get_audio_only().download()
    
    
    click.echo('Arquivo de audio baixado')


@cli.command()
@click.argument('link',type=click.STRING)
def video(link):
    yt = YouTube(link).streams.get_highest_resolution() .download()
    
    click.echo('Arquivo de video baixado')




