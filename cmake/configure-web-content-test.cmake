file(READ ${SOURCE_DIR}/testing/web-content-tests/${TEST_NAME}.js TEST_SUITE)
configure_file(
    ${SOURCE_DIR}/testing/scaffolding/web-content-test-scaffold.js.in
    tangelo/web/tests/web-content-tests/${TEST_NAME}.js
    @ONLY
)
