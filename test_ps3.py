# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import Prob1
import Prob2
import Prob3
from hashlib import sha256



class Test_Prob1:
    def test_correct_symbol(self, capsys):
        Prob1.draw_console_pyramid(3)
        captured = capsys.readouterr().out.strip()
        assert captured[-1] == '*', 'Are you not using the * symbol to build your pyramid?'

    def test_correct_number_of_rows(self, capsys):
        inputs = [1,3,8]
        for r in inputs:
            Prob1.draw_console_pyramid(r)
            captured = capsys.readouterr().out.splitlines()
            assert len(captured) == r, \
                f"You don't seem to be outputting the desired number of rows. You wanted {r} and instead printed {len(captured)}."

    def test_row_growth_rate(self, capsys):
        Prob1.draw_console_pyramid(5)
        captured = capsys.readouterr().out.splitlines()
        for i in range(len(captured)):
            assert captured[i].count('*') == 1 + 2 * i, \
                'The number of * in each row is not increasing by 2 each time'

    def test_symmetric_pyramid(self, capsys):
        Prob1.draw_console_pyramid(10)
        captured = capsys.readouterr().out.splitlines()
        start = captured[0].find('*')
        for i, row in enumerate(captured):
            assert row.find('*') == start - i, 'The left side of your pyramid is not symmetric?'
            assert row.rfind('*') == start + i, 'The right side of your pyramid is not symmetric?'

    def test_against_left_margin_at_bottom(self, capsys):
        Prob1.draw_console_pyramid(10)
        captured = capsys.readouterr().out.splitlines()
        assert captured[-1][0] == '*', \
            'Your pyramid should be against the left edge at the bottom, and it seems to not be.'


class Test_Prob2:
    def test_contains_repeated_letters(self):
        inputs = ["single", "repeating", "eerie", "shiny", "dead", "wheat", "putty"]
        sols = [False, True, True, False, True, False, True]
        for i,o in zip(inputs, sols):
            res = Prob2.contains_repeated_letters(i)
            assert res == o, \
                f"Your function should return {o} for the word {i}, but it instead returns {res}"

    def test_longest_no_repeats(self):
        out = Prob2.longest_no_repeats()
        assert out is not None, "You don't seem to be returning anything from longest_no_repeats"
        byte_output = bytes(out, 'utf-8')
        hashed = sha256(byte_output).hexdigest()
        assert hashed == "81ac598f4c30fa5fb829dc004375bd4f8d7229ac8fb5d0af7f78ea8fc22460de", \
            f"Your longest word of {out} does not seem to be correct. Does it have duplicate letters? Or are you sure it is the longest?"


class Test_Prob3:
    def test_returns_string(self):
        student = Prob3.to_obenglobish("english")
        assert type(student) == str, f"You should be returning a string, but are currently returning a {type(student)}."

    def test_easy_vowels(self):
        words = ["english", "fish", "panda"]
        sols = ["obenglobish", "fobish", "pobandoba"]
        for w,s in zip(words, sols):
            student = Prob3.to_obenglobish(w)
            assert student == s, f"{w} translated to {student} but should have been {s}."

    def test_repeat_vowels(self):
        words = ["gooiest", "fruit", "books"]
        sols = ["gobooiest", "frobuit", "bobooks"]
        for w,s in zip(words, sols):
            student = Prob3.to_obenglobish(w)
            assert student == s, f"{w} translated to {student} but should have been {s}."

    def test_ending_ees(self):
        words = ["amaze", "apple", "eerie"]
        sols = ["obamobaze", "obapple", "obeerobie"]
        for w,s in zip(words, sols):
            student = Prob3.to_obenglobish(w)
            assert student == s, f"{w} translated to {student} but should have been {s}."

    def test_different_amts_of_obs(self):
        words = ["box", "turkey", "amazing", "recommended"]
        sols = ["bobox", "toburkobey", "obamobazobing", "robecobommobendobed"]
        for w,s in zip(words, sols):
            student = Prob3.to_obenglobish(w)
            assert student == s, f"{w} translated to {student} but should have been {s}."




# Older problem 2. Kept here only in case of reuse at some point
# class Test_Prob2:
    # def test_replicates_pdf_example(self, monkeypatch, capsys):
        # input_values = ['223','251','317','636','766','607','607', '']
        # monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        # Prob2.largest_two()
        # captured = capsys.readouterr().out.splitlines()
        # assert '766' in captured[-2], f"The largest number 766 should be appearing on the second to last line of your output!"
        # assert '636' in captured[-1], f"The second-largest number 636 should be appearing on the second to last line of your output!"

    # def test_alternative_amount_of_values(self, monkeypatch, capsys):
        # input_values = ['412', '392', '744', '13', '']
        # monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        # Prob2.largest_two()
        # captured = capsys.readouterr().out.splitlines()
        # assert '744' in captured[-2], f"The largest number 744 should be appearing on the second to last line of your output!"
        # assert '412' in captured[-1], f"The second-largest number 412 should be appearing on the second to last line of your output!"
    
    # def test_alternative_orderings(self, monkeypatch, capsys):
        # input_values = [['100', '80', '50', ''], 
                        # ['100', '50', '80', ''],
                        # ['80', '100', '50', ''],
                        # ['80', '50', '100', ''],
                        # ['50', '100', '80', ''],
                        # ['50', '80', '100', '']]
        # for seq in input_values:
            # monkeypatch.setattr('builtins.input', lambda _: seq.pop(0))
            # Prob2.largest_two()
            # captured = capsys.readouterr().out.splitlines()
            # assert '100' in captured[-2], f"With inputs of {seq}, the largest number 100 should be appearing on the second to last line of your output!"
            # assert '80' in captured[-1], f"With inputs of {seq}, the second-largest number 80 should be appearing on the second to last line of your output!"

    # def test_with_negative_values(self, monkeypatch, capsys):
        # input_values = ['-42', '36', '-14', '-999999999999999999', '']
        # monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        # Prob2.largest_two()
        # captured = capsys.readouterr().out.splitlines()
        # assert '36' in captured[-2], f"The largest number 36 should be appearing on the second to last line of your output!"
        # assert '-14' in captured[-1], f"The second-largest number -14 should be appearing on the second to last line of your output!"

    # def test_equal_values(self, monkeypatch, capsys):
        # input_values = ['13', '13', '']
        # monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        # Prob2.largest_two()
        # captured = capsys.readouterr().out.splitlines()
        # assert '13' in captured[-2], f"The largest number 13 should be appearing on the second to last line of your output!"
        # assert '13' in captured[-1], f"The second-largest number 13 should be appearing on the second to last line of your output!"
