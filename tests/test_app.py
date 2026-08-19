import unittest

from main import MAX_TEXT_LENGTH, app


class ApplicationTestCase(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Text to Morse Code Converter", response.data)

    def test_conversion(self):
        response = self.client.post("/convert", data={"text": "SOS"})

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"... --- ...", response.data)

    def test_input_is_not_reflected_as_html(self):
        response = self.client.post(
            "/convert", data={"text": "<script>alert(1)</script>"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"<script>", response.data)

    def test_text_length_limit(self):
        response = self.client.post(
            "/convert", data={"text": "A" * (MAX_TEXT_LENGTH + 1)}
        )

        self.assertEqual(response.status_code, 413)

    def test_request_body_limit(self):
        response = self.client.post("/convert", data={"text": "A" * 20_000})

        self.assertEqual(response.status_code, 413)

    def test_security_headers(self):
        response = self.client.get("/")

        self.assertEqual(response.headers["X-Content-Type-Options"], "nosniff")
        self.assertEqual(response.headers["Referrer-Policy"], "no-referrer")
        self.assertIn(
            "frame-ancestors 'none'", response.headers["Content-Security-Policy"]
        )

    def test_debug_mode_is_disabled_by_default(self):
        self.assertFalse(app.debug)


if __name__ == "__main__":
    unittest.main()
