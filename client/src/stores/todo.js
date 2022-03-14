import { writable } from 'svelte/store';

const todos = writable([]);

const getTodos = (data) => {
    todos.set(data);
}

const addTodo = (data) => {
    console.log(data)
    todos.update(selectTodo => {
        let copiedTodo = [...selectTodo];
        copiedTodo = [...copiedTodo, data]
        return copiedTodo;
    });
}

const removeTodo = (id) => {
    todos.update(selectTodo => selectTodo.filter(todo => todo.id != id));
}

const updateTodo = (data) => {
    console.log(data)
    todos.update(selectTodo => {
        let copiedTodo = [...selectTodo];
        copiedTodo.find(todo => {
            if (todo.id === data.id)
                todo.title = data.title;
                todo.is_done = data.is_done;
        }
        );

        return copiedTodo;
    });
}

const updateComplete = (data) => {
    console.log(data)
    todos.update(selectTodo => {
        let copiedTodo = [...selectTodo];
        copiedTodo.find(todo => {
            if (todo.id === data.id)
                {todo.is_done = data.is_done;
                console.log(data)
              
                }
        }
        );

        return copiedTodo;
    });
}

const TodoStore = {
    todos,
    getTodos,
    addTodo,
    removeTodo,
    updateTodo,
    updateComplete,
};

export default TodoStore;