import {html} from 'heresy'
import {withAccessor} from './utils.js'

import Item from './item.js'
import { check_translation } from './api.js'

export default withAccessor('items', {

  extends: 'ul',
  includes: {Item},

  onitems() { this.render() },
  render() {
    const {items} = this
    this.html`${items.map(
      item => html`<Item oncheck=${this} .value=${item} class="list-group-item"/>`
    )}`
  },

  async oncheck(event) {
    const { currentTarget } = event
    currentTarget.value.checking = true
    this.render()
    try {
      const data = await check_translation(currentTarget.value.uid)
      currentTarget.value = data
    }
    catch (err) {
      currentTarget.value.checking = false
      this.render()
    }
  }
})