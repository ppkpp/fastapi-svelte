const getTodos = (token) => fetch(`http://localhost:8000/todos`,  {
    withCredentials: true,
    headers: {'Authorization': token,'Content-Type': 'application/json',
    'Authorization': 'Basic ' + btoa('user:user')},
    credentials: 'include',
}
);

const addTodo = (title,is_done) => fetch(`http://localhost:8000/todos`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json','Authorization': 'Basic ' + btoa('user:user')},
        withCredentials: true,
        body: JSON.stringify({
                "title": title,
                "is_done" : is_done
        })
    });


const updateTodo = (id,title, is_done) => fetch(`http://localhost:8000/todos/${id}`, {
    method: 'PUT',
    headers: {'Content-Type': 'application/json','Authorization': 'Basic ' + btoa('user:user')},
    credentials: 'include',
    body: JSON.stringify({
        "id": id,
        "title": title,
        "is_done" :is_done
    })
});

const updateComplete = (id, is_done) => fetch(`http://localhost:8000/todos/${id}`, {
    method: 'PUT',
    headers: {'Content-Type': 'application/json','Authorization': 'Basic ' + btoa('user:user')},
    credentials: 'include',
    body: JSON.stringify({
        "id": id,
        "is_done" :is_done
    })
});


const deleteTodo = (id) =>fetch(`http://localhost:8000/todos/` + id, {
withCredentials: true,
headers: {'Content-Type': 'application/json','Authorization': 'Basic ' + btoa('user:user')},
credentials: 'include',
method: 'DELETE',
});

const TodoApi ={
    getTodos,
    addTodo,
    deleteTodo,
updateTodo,
updateComplete,

};

export default TodoApi;