import translators as ts
from check_language import check_text_language

translators = ['deepl', 'google', 'cloudTranslation', 'iciba', 'modernMt', 'qqFanyl', 'sysTran', 'translateCom']


def translate(text: str, translator: str = 'deepl') -> str:
    try:
      if(text.upper() == text.lower()): return text
      from_lang = check_text_language(text)
      if(from_lang == 'none'): return text
      to_lang = 'en' if from_lang == 'uk' else 'uk'
      

      result = ts.translate_text(text, translator, from_language=from_lang, to_language=to_lang)
      # print(result)
      return result
    except Exception as e:
      translationIndex = translators.index(translator)+1
      if(translationIndex >= len(translators)): return text
      newTranslator = translators[translationIndex]
      return translate(text, newTranslator)
