from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class Round1InternationalizationContractTests(unittest.TestCase):
    def test_english_translation_layer_and_real_language_actions_exist(self):
        english_dir = ROOT / "game" / "tl" / "english"
        self.assertTrue(english_dir.is_dir())
        self.assertTrue(any(english_dir.glob("*.rpy")))

        screens = (ROOT / "game" / "screens.rpy").read_text(encoding="utf-8-sig")
        self.assertIn('Language(None)', screens)
        self.assertIn('Language("english")', screens)
        self.assertNotRegex(screens, r'Language\("(?:chinese-traditional|vietnamese)"\)')

    def test_round1_translation_contains_core_ui_and_prologue(self):
        translation = "\n".join(
            path.read_text(encoding="utf-8-sig")
            for path in sorted((ROOT / "game" / "tl" / "english").glob("*.rpy"))
        )
        for source, target in (
            ("开始游戏", "Start Game"),
            ("设置", "Preferences"),
            ("江湖小镇之凰龙府", "Jianghu Town: Huanglongfu"),
            ("大明国，庆丰年间。", "In the Qingfeng years of the Great Ming Realm."),
            ("王放", "Wang Fang"),
            ("左婉", "Zuo Wan"),
        ):
            self.assertIn(source, translation)
            self.assertIn(target, translation)

    def test_confirmed_canonical_spellings_and_deprecated_forms_are_documented(self):
        glossary = (ROOT / "docs" / "i18n" / "JIANGHU_TOWN_GLOSSARY_V0_1.md").read_text()
        self.assertRegex(
            glossary,
            r"\| town_kaian \| 开庵镇 \| .* \| 主创确认的正式名称 \| .* \| 开安镇 \|",
        )
        self.assertRegex(
            glossary,
            r"\| peak_leiyun \| 雷云峰 \| .* \| 主创确认的正式名称 \| .* \| 雷云锋、Thundercloud Peak \|",
        )


if __name__ == "__main__":
    unittest.main()
