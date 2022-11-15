import { writable } from 'svelte/store'

// local storage users
const storage_key = 'persist_user'
const stored = localStorage.getItem(storage_key)

export const user = writable(JSON.parse(stored) ?? '')
user.subscribe(value => {
    localStorage.setItem(storage_key, JSON.stringify(value))
})


export const logout = () => {
    user.set('')
    localStorage.removeItem(storage_key)
}