from urllib.request import urlopen
import json
import click
import re

BASE_URL = "https://glosbe.com/gapi/translate"


class Meaning:
    def __init__(self, phrase, japanese, english=None):
        self.phrase = phrase
        self.japanese = japanese
        self.english = english

    def look_up(self):
        print("* " + self.japanese + ' *')
        if self.english:
            self._extract_mean()
        else:
            print("適切な英語の説明がありませんでした。")

    def _extract_mean(self):
        for i, mean in enumerate(self.english, 1):
            text = mean['text']
            eg_regex = re.search('e.g.', text)
            esp_regex = re.search('esp.', text)
            if not any([eg_regex, esp_regex]):
                text = text.replace('. ', '.\n\t')
            else:
                text = mean['text']

            if mean['language'] == 'ja':
                continue
            print(f"意味{i} : {text}")


def get_url(phrase):
    """Glosbe API により、引数に与えられた単語の翻訳を取得

    :param phrase:
    """
    tarnslated_ja = "?from=en&dest=ja"
    phrase_arg = f"&phrase={phrase}"
    url = f"{BASE_URL}{tarnslated_ja}&format=json{phrase_arg}&pretty=true"
    return url


def load_json(json_data):
    loaded = json.loads(json_data)['tuc']
    if not loaded:
        raise click.exceptions.BadParameter("検索した結果,見つかりませんでした")

    for json_dict in loaded:
        yield json_dict


@click.command()
@click.option('--phrase', '-p', default='python', help='検索したい文字列が必要です')
def cmd(phrase):
    num = click.prompt('検索結果の出力数(1〜7)を入力して下さい', type=int)
    if num == 0: raise click.BadParameter("出力数は1以上にしてください")
    if num > 7: raise click.BadParameter("そんなに出力できません。")

    url = get_url(phrase)
    response = urlopen(url)
    json_data = response.read().decode("utf-8")
    data = load_json(json_data)

    for counter, mean_pair in enumerate(data):

        if counter == 0: print(f'=== {phrase}の意味 ==================')
        if counter > num - 1: break

        try:
            japanese = mean_pair['phrase']['text']
        except:
            raise click.BadParameter("見つかりませんでした")
        english = mean_pair['meanings'] if 'meanings' in mean_pair else None
        mean = Meaning(phrase, japanese, english)
        mean.look_up()
        print("=================================")


def main():
    cmd()


if __name__ == '__main__':
    main()
