from py3langid.langid import LanguageIdentifier, MODEL_FILE

identifier = LanguageIdentifier.from_pickled_model(MODEL_FILE, norm_probs=True)

def detect_language_with_langid(line):
    lang, prob = identifier.classify(line)
    return lang, prob

def detect_languages(text):
    detected_languages = set()  
    for line in text.split('\n'):
        line = line.strip()
        if line:  
            lang, prob = detect_language_with_langid(line)
            if prob > 0.8:  
                detected_languages.add(lang)
    return list(detected_languages)
