def get_words_number(string):
        return len(string.split())

def get_char_count(string):
        char_count = {}
        for raw_char in string:
                char = raw_char.lower()
                if char in char_count:
                        char_count[char] += 1
                else:
                        char_count[char] = 1
        return char_count
def sort_dict(dict):
        def sort_on(dict):
            return dict["count"]
        result = []
        for key in dict:
                if key.isalpha():
                    result.append({"char":key,"count":dict[key]})
        result.sort(reverse=True, key=sort_on)
        return result