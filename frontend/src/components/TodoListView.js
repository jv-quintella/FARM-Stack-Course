import TodoItem from './Todo'

// Render the todo list by creating a TodoItem component for each task.
export default function TodoView(props) {
    return (
        <div>
            <ul>
                {props.todoList.map(todo => <TodoItem todo={todo} />)}
            </ul>
        </div>
    )
}