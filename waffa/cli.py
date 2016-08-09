import os
import click
import wolframalpha


@click.command()
@click.argument('query', nargs=-1)
def cli(query):
    client = wolframalpha.Client(os.getenv('WAFFA_APP_ID'))
    result = client.query(query=' '.join(query))
    try:
        print(next(result.results).text)
    except StopIteration:
        print('No results')
