import { steamID, steamAvatar, steamName } from "./stores";

let id: string;
steamID.subscribe(value => {
    id = value
})

export async function load() {
    if (id) {
        let data = await fetch(`http://localhost:8003/user/info/${id}`);
		let jdata = await data.json();
            steamName.set(jdata.response.players[0].personaname)
            steamAvatar.set(jdata.response.players[0].avatarfull)
    } else {
        return
    }
  }