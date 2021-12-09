def generate_hashtag(s):
    if s in '' or len(s) >= 140:
        return False
    else:
        return '#' + ''.join(map(lambda x: str(x).title() ,s.split()))

print(generate_hashtag('Codewars Is Nice'))