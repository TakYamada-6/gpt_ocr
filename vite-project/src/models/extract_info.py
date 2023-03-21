import configparser
import openai


CONF_FILE = "config.ini"
RESUME_FILE = "../../../resumes/BU2680284.txt"

# APIキーの設定
config = configparser.ConfigParser()
config.read(CONF_FILE)
api_key = config["openai"]["api_key"]
openai.api_key = api_key


def extract_info(resume_text):
    # クエリを定義
    text = resume_text
    # input_text = f"以下はPDFから抽出したテキストです:\n{text}\n\n" \
    #              "このテキストを要約して日本語の職務経歴書として以下の形にフォーマットしてください。テキストに載っている情報以外を含めてはいけません。必ず指示に従ってください。：\n" \
    #              "要約：必ず40文字以内で彼の経歴の要約強みや使用言語、ツールなどのスキルを書く。彼が何をアピールしているかを推測し必ずそこに触れる。\n" \
    #              "スキル：具体的なプログラミング言語やフレームワーク、使用可能なツールを網羅する。\n" \
    #              "職務経歴：会社名/ポジション（在籍期間）具体的な業務内容：彼の経験したプロジェクトを網羅する。150文字以内\n" \
    #              "学歴：学歴と学位を必ず記述する\n" \
    #              "語学・資格：TOEICの点数や各種資格を箇条書きで必ず網羅する。"\
    #              "\n\nテキストから読み取れる情報以外を付け加えてはいけません。" \
    #              "すべての経歴・学歴、語学・資格を漏れなく含めてください。" \
    #              "上限文字数に必ず収めてください。最後に事実のみが含まれていること＆漏れがないことを確認して生成してください:"

    input_text = f"以下はPDFから抽出したテキストです:\n{text}\n\n" \
                 "このテキストを日本語で要約してください。このテキストに載っている情報以外を含めてはいけません。必ず指示に従ってください。：\n" \
                 "必ず40文字以内で彼の経歴からわかる実績や強みや使用言語、ツールなどのスキルを書く。彼が何をアピールしているかを推測し必ずそこに触れる。生成されたテキストを見たとき彼が喜ぶように作る。\n" \
                 "上限文字数に必ず収めてください。最後に事実のみが含まれていること＆漏れがないことを確認して生成してください:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        n=1,
        stop=None,
        temperature=0.3,
        messages=[
            {"role": "user", "content": input_text}
        ]
    )

    extracted_info = response["choices"][0]["message"]["content"]
    return extracted_info
