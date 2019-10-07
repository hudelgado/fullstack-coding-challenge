export default {
  extends: 'header',
  render() {
    this.html`
      <h1>Unbabel API Translator example</h1>
      <div class="container-fluid">
        <div class="container-body form-group">
          <label for="textToTranslate">Text to Translate</label>
          <input class="form-control" id="textToTranslate" />
          <label for="textToTranslate">(EN) English => (ES) Spanish</label>
        </div>
        <div class="container-sidebar">
          <div class="spinner-border" role="status">
            <span class="sr-only">Loading...</span>
          </div>
        </div>
      </div>
    `
  }
}