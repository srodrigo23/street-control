function addfakeuser(){
  const table = document.getElementById('usersTable').getElementsByTagName('usersTableBody')[0];
  fetch("/users/add_user") 
    .then(response => response.json()) 
    .then(data => {
      $("#usersTableBody").prepend(
          `<tr class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
          <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
            ${data.name}
          </th>
          <td class="px-6 py-4">
            ${data.user_name}
          </td>
          <td class="px-6 py-4">
            ${data.last_connection}
          </td>
          <td class="px-6 py-4">
              <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
          </td>
        </tr>`
      )
      console.log(data)
    })
    .catch(error => console.error(error))
}