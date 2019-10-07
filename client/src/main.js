import {ref} from 'heresy'
import {withAccessor} from './utils.js'

import List from './list.js'

export default withAccessor('data', {
  extends: 'section',
  includes: {List},
  ondata() { this.render() },
  render() {
    this.html`
      <List
        class="list-group"
        ref=${ref(this, 'list')}
        .items=${this.data.items}
      />
    `
  }
})