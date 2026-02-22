from pages.twitch_page import TwitchPage


class TestTwitch:

    def test_twitch_mobile(self, driver, request):
        twitch_page = TwitchPage(driver)
        twitch_page.load()
        driver.fullscreen_window()
        twitch_page.handle_keep_using_web_popup()
        twitch_page.accept_cookies()
        assert twitch_page.is_loaded()

        twitch_page.click_search_icon()
        twitch_page.click_search_input()
        twitch_page.enter_search_query("StarCraft II")
        twitch_page.select_all_channels()
        twitch_page.scroll_down(scroll_number=2)
        streamer_page = twitch_page.open_streamer_page()
        streamer_page.close_optional_modal()
        streamer_page.is_loaded()
        streamer_page.take_screenshot(test_name=request.node.name, pic_name="streamer_page")
