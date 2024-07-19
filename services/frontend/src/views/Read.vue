<template>
  <section>
    <h1>READ SONG</h1>
    <h2>Read all Songs</h2>
    <button @click="fetchSongs()" class="btn btn-primary">getAllSongs</button>

    <table v-if="view_songs == true" class="table">
      <thead class="thead-dark">
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Artist</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="song in songs" :key="song.id">
          <td>{{ song.id }}</td>
          <td>{{ song.name }}</td>
          <td>{{ song.artist }}</td>
        </tr>
      </tbody>
    </table>
  </section>

  <section>
    <h2>Read Song by ID</h2>
    <div>
      <input type="text" v-model="this.id" placeholder="Enter Song ID" />
      <button @click="fetchSong()" class="btn btn-primary">getSong</button>
    </div>

    <div v-if="cur_song != null">
      Your Song name is <span style="color: red">{{ cur_song.name }}</span> and artist name is
      <span style="color: blue">{{ cur_song.artist }}</span
      >.
    </div>
  </section>
</template>

<script>
import { defineComponent } from 'vue'
import { mapGetters, mapActions } from 'vuex'
import _ from 'lodash'

export default defineComponent({
  name: 'read_song',
  data() {
    return {
      view_songs: false,
      cur_song: null,
      id: ''
    }
  },
  computed: {
    ...mapGetters({ songs: 'stateSongs', song: 'stateSong' })
  },
  methods: {
    ...mapActions(['getSongs', 'getSong']),

    async fetchSongs() {
      try {
        await this.getSongs()
        this.view_songs = true
        console.log('Songs fetched successfully')
      } catch (error) {
        console.error(error)
      }
    },
    async fetchSong() {
      try {
        await this.getSong(this.id)
        this.cur_song = _.cloneDeep(this.song)
        console.log('Song fetched successfully')
      } catch (error) {
        this.id = ''
        this.cur_song = null
      }
    }
  }
})
</script>
