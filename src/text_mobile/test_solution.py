from text_mobile.solution import convert_text, to_key_press, global_mobile_dictionary

def test_solution():
    #Test case
    assert to_key_press("H",global_mobile_dictionary) == "44"
    assert to_key_press(" ",global_mobile_dictionary) == "0"
    assert convert_text("HELLO, WORLD!") == "44·33·555·555·666·11·0·9·666·777·555·3·1111"