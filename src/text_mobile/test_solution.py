from text_mobile.solution import (
    clean_to_list,
    convert_number_to_text,
    convert_text_to_number,
    to_key_press_number,
    to_key_press_text,
    global_mobile_dictionary,
)


def test_solution():
    # Test case
    assert clean_to_list("3·6·999·8·777·666·") == ["3", "6", "999", "8", "777", "666"]
    assert to_key_press_text("H", global_mobile_dictionary) == "44"
    assert to_key_press_text(" ", global_mobile_dictionary) == "0"
    assert (
        convert_text_to_number("HELLO, WORLD!")
        == "44·33·555·555·666·11·0·9·666·777·555·3·1111·"
    )
    assert convert_text_to_number("DMYTRO") == "3·6·999·8·777·666·"
    assert convert_number_to_text("3·6·999·8·777·666·") == "DMYTRO"
    assert to_key_press_number("44", global_mobile_dictionary) == "H"
