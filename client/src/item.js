  
import {withAccessor} from './utils.js'

export default withAccessor('value', {

  extends: 'li',

  onvalue() { this.render() },
  onclick(event) {
    event.stopPropagation()
    this.dispatchEvent(new Event('check'))
  },

  render() {
    const {text, translation, status, checking} = this.value
    this.classList.toggle('translated', status === 'completed')
    this.classList.toggle('checking', checking === true)
    this.html`
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">${text}</h5>
      <button class="update" onclick=${this}>
        <span class="oi oi-loop-circular"></span>
      </button>
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
      <span class="${getBadgeStatus(status)}">${status}</span>
    </div>
    <p class="mb-1">${translation}</p>`
  }
})

function getBadgeStatus(status) {
  var badgeStatus = 'badge badge-'
  return `${badgeStatus}${status === 'completed'
    ? 'success' : 'primary'}`
}