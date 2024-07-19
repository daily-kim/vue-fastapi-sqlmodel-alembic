<template>
  <section>
    <h1>DELETE SONG</h1>
    <h2>1. Read song</h2>
    <div>
      <input type="text" v-model="id" placeholder="Enter Song ID" />
      <button @click="fetchSong()" class="btn btn-primary">getSong</button>
    </div>
    <div v-if="cur_song">
      Your Song name is <span style="color: red">{{ cur_song.name }}</span> and artist name is
      <span style="color: blue">{{ cur_song.artist }}</span
      >.
    </div>

    <h2>2. Delete song</h2>
    <div>
      <button @click="removeSong()" class="btn btn-primary">Delete Song</button>
    </div>
  </section>
</template>
<script>
import { defineComponent } from 'vue'
import { mapGetters, mapActions } from 'vuex'
import _ from 'lodash'

export default defineComponent({
  name: 'delete_song',
  data() {
    return {
      id: '',
      cur_song: null
    }
  },
  computed: {
    ...mapGetters({ songs: 'stateSongs', song: 'stateSong' })
  },
  methods: {
    ...mapActions(['getSong', 'deleteSong']),
    async fetchSong() {
      try {
        await this.getSong(this.id)
        this.cur_song = _.cloneDeep(this.song)
        console.log('Song fetched successfully')
      } catch (error) {
        this.cur_song = null
      }
    },
    async removeSong() {
      await this.deleteSong(this.id)
      this.cur_song = null
      console.log('Song delete successfully')
    }
  }
})
</script>
