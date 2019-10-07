import { define, ref } from 'heresy'


import { data } from './utils.js'
import Header from './header.js'
import Main from './main.js'
import { get_translations, create_translation } from './api.js'


define('TranslationApp', {

  extends: 'section',
  includes: {Header, Main},
  style: (self) => `
    ${self} ul > li.translated .update {
      display: none;
    }
    ${self} ul > li.checking .update,
    ${self} ul > li:not(.checking) .spinner-border {
      display: none;
    }
    ${self}:not(.inserting) header .container-sidebar {
      display: none;
    }
  `,

  async oninit() {
    this.data = data([this.id || '', this.is].join(':'))
    this.header = ref()
    this.main = ref()
    this.footer = ref()
    this.currentPage = 1
    await this.update_translations()
  },

  render() {
    this.html`
    <Header class="header" ref=${this.header} onchange=${this}/>
    <Main class="main" ref=${this.main} onchange=${this} .data=${this.data}/>
    `
  },

  async create(text) {
    this.classList.add('inserting')
    try {
      await create_translation({
        source_language: 'en',
        target_language: 'es',
        text
      })
      await this.update_translations()
    }
    catch(err) {}
    finally {
      this.classList.remove('inserting')
    }

    
  },
  async update_translations() {
    this.data.items = await get_translations()
    this.render()
  },

  onchange(event) {
    const {currentTarget, target} = event
    switch (currentTarget) {
      case this.header.current:
        const value = target.value.trim()
        if (value && !getItem(this.data.items, value)) {
          target.value = ''
          this.create(value)
        }
        break
    }
    this.render()
  },
  onclick (event) {
    const {currentTarget, target} = event

  }
})

function getItem(items, text) {
  return items.some(item => item.text === text)
  this.currentPage = this.currentPage + 1
}