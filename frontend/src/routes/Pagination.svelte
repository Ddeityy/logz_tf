<script lang="ts">
	import { onMount } from 'svelte';
	import { createEventDispatcher } from 'svelte';

	export let currentPage: number;
	let total: number;
	let pages: number;
	let items: any;
	let rightArrow = 'right.png';
	let leftArrow = 'back.png';
	const dispatch = createEventDispatcher();

	function paginate(page: number) {
		dispatch('message', {
			text: page
		});
	}

	const arrayRange = (length: number) => {
		let arr: any = [];
		for (let index = 0; index < length - 1; index++) {
			arr.push(index + 2);
		}
		return arr;
	};
	onMount(async () => {
		let res = await fetch('http://127.0.0.1:8003/total');
		total = parseInt(await res.text());
		pages = Math.floor(total / 20);
		items = arrayRange(pages);
	});
</script>

{#if total && pages}
	<div class="pagination">
		<!-- svelte-ignore a11y-click-events-have-key-events -->
		<!-- svelte-ignore a11y-invalid-attribute -->
		<ul>
			{#if currentPage === 1}
				<li><span style="color: #555555"><strong>{currentPage}</strong></span></li>
				{#each arrayRange(5) as num}
					<li>
						<a href="#" on:click={() => paginate(currentPage + num - 1)}>{currentPage + num - 1}</a>
					</li>
				{/each}
				<li><span style="color: #555555"><strong>...</strong></span></li>
				<li><a href="#" on:click={() => paginate(items.length + 1)}>{items.length + 1}</a></li>
				<li>
					<img on:click={() => paginate(currentPage + 1)} src={rightArrow} alt="right arrow" />
				</li>
			{:else if currentPage === 2}
				<li>
					<img on:click={() => paginate(currentPage - 1)} src={leftArrow} alt="left arrow" />
				</li>
				<li><a href="#" on:click={() => paginate(currentPage - 1)}>{currentPage - 1}</a></li>
				<li><span style="color: #555555"><strong>{currentPage}</strong></span></li>
				{#each arrayRange(4) as num}
					<li>
						<a href="#" on:click={() => paginate(currentPage + num - 1)}>{currentPage + num - 1}</a>
					</li>
				{/each}
				<li><span style="color: #555555"><strong>...</strong></span></li>
				<li><a href="#" on:click={() => paginate(items.length + 1)}>{items.length + 1}</a></li>
				<li>
					<img on:click={() => paginate(currentPage + 1)} src={rightArrow} alt="right arrow" />
				</li>
			{:else if currentPage >= 3 && currentPage <= items.length - 2 && currentPage <= 5}
				<li>
					<img on:click={() => paginate(currentPage - 1)} src={leftArrow} alt="left arrow" />
				</li>

				<li><a href="#" on:click={() => paginate(currentPage - 2)}>{currentPage - 2}</a></li>
				<li><a href="#" on:click={() => paginate(currentPage - 1)}>{currentPage - 1}</a></li>
				<li><span style="color: #555555"><strong>{currentPage}</strong></span></li>
				<li><a href="#" on:click={() => paginate(currentPage + 1)}>{currentPage + 1}</a></li>
				<li><a href="#" on:click={() => paginate(currentPage + 2)}>{currentPage + 2}</a></li>
				<li><span style="color: #555555"><strong>...</strong></span></li>
				<li><a href="#" on:click={() => paginate(items.length + 1)}>{items.length + 1}</a></li>
				<li>
					<img on:click={() => paginate(currentPage + 1)} src={rightArrow} alt="right arrow" />
				</li>
			{:else if currentPage >= 5 && currentPage <= items.length - 2}<li>
					<img on:click={() => paginate(currentPage - 1)} src={leftArrow} alt="left arrow" />
				</li>
				<li><a href="#" on:click={() => paginate(1)}>1</a></li>
				<li><span style="color: #555555"><strong>...</strong></span></li>
				<li><a href="#" on:click={() => paginate(currentPage - 2)}>{currentPage - 2}</a></li>
				<li><a href="#" on:click={() => paginate(currentPage - 1)}>{currentPage - 1}</a></li>
				<li><span style="color: #555555"><strong>{currentPage}</strong></span></li>
				<li><a href="#" on:click={() => paginate(currentPage + 1)}>{currentPage + 1}</a></li>
				<li><a href="#" on:click={() => paginate(currentPage + 2)}>{currentPage + 2}</a></li>
				<li><span style="color: #555555"><strong>...</strong></span></li>
				<li><a href="#" on:click={() => paginate(items.length + 1)}>{items.length + 1}</a></li>
				<li>
					<img on:click={() => paginate(currentPage + 1)} src={rightArrow} alt="right arrow" />
				</li>
			{:else if currentPage <= items.length - 1}
				<li>
					<img on:click={() => paginate(currentPage - 1)} src={leftArrow} alt="left arrow" />
				</li>
				<li><a href="#" on:click={() => paginate(currentPage - 2)}>{currentPage - 2}</a></li>
				<li><a href="#" on:click={() => paginate(currentPage - 1)}>{currentPage - 1}</a></li>
				<li><span style="color: #555555"><strong>{currentPage}</strong></span></li>
				<li><a href="#" on:click={() => paginate(currentPage + 1)}>{currentPage + 1}</a></li>
				<li><a href="#" on:click={() => paginate(currentPage + 2)}>{currentPage + 2}</a></li>
			{:else if currentPage === items.length}
				<li>
					<img on:click={() => paginate(currentPage - 1)} src={leftArrow} alt="left arrow" />
				</li>
				{#each arrayRange(4) as _}
					<li>
						<a href="#" on:click={() => paginate(currentPage - 1)}>{currentPage - 1}</a>
					</li>
				{/each}
				<li><span style="color: #555555"><strong>{currentPage}</strong></span></li>
				<li><a href="#" on:click={() => paginate(currentPage + 1)}>{currentPage + 1}</a></li>
			{:else if currentPage === items.length + 1}
				<li>
					<img on:click={() => paginate(currentPage - 1)} src={leftArrow} alt="left arrow" />
				</li>
				{#each arrayRange(5).reverse() as num}
					<li>
						<a href="#" on:click={() => paginate(currentPage - num + 1)}>{currentPage - num + 1}</a>
					</li>
				{/each}
				<li><span style="color: #555555"><strong>{currentPage}</strong></span></li>
			{/if}
		</ul>
	</div>
{/if}

<style lang="scss">
	.pagination {
		display: flex;
		background-color: white;
		padding-right: 35px;
		margin: 10px;
		border-radius: 5px;
		width: fit-content;
		margin-left: -30px;
		ul {
			display: inline-block;
			li {
				display: inline;
				a,
				span,
				img {
					float: left;
					padding: 4px 12px;
					line-height: 20px;
					text-decoration: none;
					background-color: #ffffff;
					border: 1px solid #dddddd;

					color: #dd4814;
				}
				img {
					max-width: 19.5px;
					cursor: pointer;
				}

				a:hover,
				img:hover {
					color: #97310e;
					background-color: #eeeeee;
				}
			}
		}
	}
</style>
