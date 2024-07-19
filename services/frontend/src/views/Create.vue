<template>
  <section>
    <h1>CREATE SONG</h1>
    <form @submit="addSong">
      <div class="mb-3">
        <label for="name" class="form-label">Song Name:</label>
        <input type="text" name="name" v-model="song.name" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="artist" class="form-label">Artist Name:</label>
        <input type="text" name="artist" v-model="song.artist" class="form-control" />
      </div>
      <button type="submit" class="btn btn-primary">Add</button>
    </form>
  </section>
</template>

<script>
import { defineComponent } from 'vue'
import { mapActions } from 'vuex'

export default defineComponent({
  name: 'create_song',
  data() {
    return {
      song: {
        name: '',
        artist: ''
      }
    }
  },
  methods: {
    ...mapActions(['createSong']),
    async addSong() {
      try {
        await this.createSong(this.song)
        console.log('Song added successfully')
      } catch (error) {
        console.error(error)
      }
    }
  }
})
</script>
