<script>
	export let name;
	import { onMount, onDestroy } from "svelte";
	import TodoApi from "../src/services/TodoApi";
	import TodoStore from "../src/stores/todo";
	let todos;
	let create_title = "";
	onMount(async () => {
		await TodoApi.getTodos()
			.then((r) => r.json())
			.then((data) => {
				TodoStore.getTodos(data);
			});
	});

	const unsub = TodoStore.todos.subscribe((data) => {
		console.log(data);
		todos = data;
	});

	const createTask = () => {
		TodoApi.addTodo(create_title, false)
			.then((response) => response.json())
			.then((data) => {
				TodoStore.addTodo(data);
				create_title = "";
			})
			.catch((error) => {
				console.error("Error:", error);
			});
	};

	const handleChange = (id, is_done) => {
		TodoApi.updateComplete(id, !is_done)
			.then((response) => response.json())
			.then((data) => {
				console.log("Success:", data);
				TodoStore.updateComplete(data)
			})
			.catch((error) => {
				console.error("Error:", error);
			});
	};

	const updateClassroom = async () => {
		user_ids = [];
		for (let user of select_user) user_ids.push(user["value"]);
		let access_token = localStorage.getItem("access_token");
		let token = "Bearer " + access_token;
		ClassroomApi.updateClassroom(
			id,
			class_name,
			grade,
			class_type["value"],
			user_ids,
			course_id,
			token
		)
			.then((response) => response.json())
			.then((data) => {
				cancel();
				console.log("Success:", data);
			})
			.catch((error) => {
				console.error("Error:", error);
			});
	};

	const deleteTodo = async (id) => {
		TodoApi.deleteTodo(id).then((r) => {
      if (r.ok) TodoStore.removeTodo(id);
    });
	}
</script>

<main>
	<div class="container">
		<div>
			<p>
				<label for="new-task">Add Item</label><input
					id="new-task"
					type="text"
					bind:value={create_title}
				/><button on:click={() => createTask()}>Add</button>
			</p>
		</div>
		<div class="todo_list">
			<ul>
				{#each todos as todo}
					<li>
						<!--TO DO ITEM START-->
						<label>
							<input
								type="checkbox"
								class="hidden_real_check"
								checked={todo.is_done}
								on:change={handleChange(todo.id, todo.is_done)}
							/>
							<div class="todo_element">
								<span class="customized_ckeck">
									<span class="checkbox">
										<span class="internal_one" />
										<span class="internal_two" />
									</span>
								</span>
								<span class="element_title">{todo.title}</span>
								<span class="element_action">
									<button on:click={() => deleteTodo(todo.id)}>Delete</button>
								</span>
							</div>
						</label>
					
					</li>
				{/each}
			</ul>
		</div>
	</div>
</main>

<style>
	body {
		background: #f5f5f5;
	}

	.container {
		width: 100%;
		max-width: 400px;
		margin: 50px auto;
	}

	.todo_list {
		background: #fff;
		box-shadow: 0 0 27px #ccc;
	}

	.todo_list ul {
		list-style: none;
		padding: 0;
	}

	.todo_list ul li label {
		display: block;
		position: relative;
		padding: 0 10px;
	}

	.hidden_real_check {
		width: 100%;
		height: 100%;
		opacity: 0;
		position: absolute;
	}

	.todo_element {
		border-bottom: 1px solid #ddd;
		padding: 10px 0;
	}
	.todo_list ul li:last-child .todo_element {
		border-bottom: none;
	}

	.customized_ckeck {
		display: inline-flex;
		width: 15%;
		height: 2em;
		align-items: center;
		justify-content: flex-end;
	}
	.element_title {
		display: inline-block;
		width: 65%;
		height: 2em;
		float: center;
		font-family: "Open Sans", sans-serif;
		line-height: 2em;
		position: relative;
		color: #333;
		letter-spacing: 1px;
	}

	.element_action {
		display: inline-block;
		height: 2em;
		float: right;
		font-family: "Open Sans", sans-serif;
		line-height: 2em;
		position: relative;
		color: #333;
		letter-spacing: 1px;
	}

	.element_title:after {
		content: "";
		position: absolute;
		top: 50%;
		height: 2px;
		width: 0;
		background-image: linear-gradient(90deg, #4facfe, #00f2fe);
		left: -5px;
		z-index: 2;
		transition: 0.3s;
	}

	.element_title:before {
		content: "";
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background: rgba(255, 255, 255, 0.7);
		z-index: 1;
		transition: 0.3s;
		opacity: 0;
	}

	.todo_list
		ul
		li
		label
		.hidden_real_check:checked
		+ .todo_element
		.element_title::after {
		width: 90%;
	}
	.todo_list
		ul
		li
		label
		.hidden_real_check:checked
		+ .todo_element
		.element_title::before {
		opacity: 1;
	}
	.checkbox {
		width: 25px;
		height: 25px;
		margin-right: 5px;
		position: relative;
		transition: 0.1s;
		transition-delay: 0.3s;
	}
	.checkbox span[class*="internal_"] {
		position: absolute;
		top: 0;
		right: 0;
		left: 0;
		bottom: 0;
	}
	.checkbox:after {
		content: "✔";
		position: absolute;
		top: 0;
		left: 2px;
		right: -2px;
		bottom: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #4facfe;
		transform: scale(0);
		transition: 0.4s;
	}
	.checkbox:before {
		content: "";
		position: absolute;
		top: 0;
		left: 2px;
		right: -2px;
		bottom: 0;
		border-radius: 50%;
		border: 5px dotted #4facfe;
		transform: scale(0) rotate(0);
		transition: 0.5s;
		transition-delay: 0.3s;
	}
	.checkbox span[class*="internal_"]::after,
	.checkbox span[class*="internal_"]::before {
		content: "";
		position: absolute;
		top: 0px;
		left: 2px;
		height: 100%;
		width: 100%;
		border-radius: 50%;
		border: 2px solid transparent;
		transform: rotate(45deg);
		box-sizing: border-box;
	}
	.checkbox span.internal_one::after {
		border-top-color: #4facfe !important;
		transition: 0.4s;
	}
	.checkbox span.internal_one::before {
		border-left-color: #4facfe !important;
		transition: 0.3s;
		transition-delay: 0.1s;
	}
	.checkbox span.internal_two::after {
		border-bottom-color: #4facfe !important;
		transition: 0.2s;
		transition-delay: 0.2s;
	}
	.checkbox span.internal_two::before {
		border-right-color: #4facfe !important;
		transition: 0.1s;
		transition-delay: 0.3s;
	}
	.todo_list
		ul
		li
		label
		.hidden_real_check:checked
		+ .todo_element
		.checkbox
		.internal_one:after {
		transform: rotate(-225deg);
	}
	.todo_list
		ul
		li
		label
		.hidden_real_check:checked
		+ .todo_element
		.checkbox
		.internal_one:before {
		transform: rotate(-135deg);
	}
	.todo_list
		ul
		li
		label
		.hidden_real_check:checked
		+ .todo_element
		.checkbox
		.internal_two:after {
		transform: rotate(-45deg);
	}
	.todo_list
		ul
		li
		label
		.hidden_real_check:checked
		+ .todo_element
		.checkbox
		span[class*="internal_"]:after,
	.todo_list
		ul
		li
		label
		.hidden_real_check:checked
		+ .todo_element
		.checkbox
		span[class*="internal_"]:before {
		border-color: transparent !important;
	}
	.todo_list
		ul
		li
		label
		.hidden_real_check:checked
		+ .todo_element
		.checkbox:after {
		transform: scale(1);
	}
	.todo_list
		ul
		li
		label
		.hidden_real_check:checked
		+ .todo_element
		.checkbox:before {
		transform: scale(1.6) rotate(-90deg);
		opacity: 0;
	}

	label[for="new-task"] {
		color: #333;
		font-weight: 700;
		font-size: 15px;
		border-bottom: 2px solid #333;
		padding: 30px 0 10px;
		margin: 0;
		text-transform: uppercase;
	}
	input[type="text"] {
		margin: 0;
		font-size: 18px;
		line-height: 18px;
		height: 18px;
		padding: 10px;
		border: 1px solid #ddd;
		background: #fff;
		border-radius: 6px;
		font-family: Lato, sans-serif;
		color: #888;
	}
	input[type="text"]:focus {
		color: #333;
	}

	/* New Task */
	label[for="new-task"] {
		display: block;
		margin: 0 0 20px;
	}
	input#new-task {
		float: left;
		width: 318px;
	}

	p > button:hover {
		color: #0fc57c;
	}

	input,
	button {
		outline: none;
	}
	button {
		background: none;
		border: 0px;
		color: #888;
		font-size: 15px;
		width: 60px;
		margin: 10px 0 0;
		font-family: Lato, sans-serif;
		cursor: pointer;
	}
	button:hover {
		color: #333;
	}
</style>
