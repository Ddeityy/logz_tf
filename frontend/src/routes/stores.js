import { persisted } from 'svelte-local-storage-store';

export const steamID = persisted('id', '');
export const steamName = persisted('username', '');
export const steamAvatar = persisted('avatar', '');
