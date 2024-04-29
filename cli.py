import click
import json_manager
@click.group()
def cli():
    pass

#crear usuarios
@cli.command()
@click.option('--name',required=True,help='Name of the user')
@click.option('--lastname',required=True,help='Lastname of the user')
@click.pass_context #manejo de errores con parametros
def create_users(ctx,name,lastname):
    if not name or not lastname:
        ctx.fail('The name and lastname are required')
    else:
        data = json_manager.read_json()
        new_id = len(data)+1
        new_user = {
            'id': new_id,
            'name': name,
            'lastname': lastname
        }
        data.append(new_user)
        json_manager.write_json(data)
        print(f"User {name} {lastname} create successfully")
        
        
#Listar todo el arcgivo json
@cli.command()
def  list_users():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")
        
#Listar un usuario por id
@cli.command()
@click.argument('id',type=int)
def list_user(id):
    data = json_manager.read_json()
    user = next ((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"User with id {id} not found")
    else:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")

#Eliminar usuario  
@cli.command()
@click.argument('id',type=int)
def delete_user(id):
    data = json_manager.read_json()
    user = next ((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"User with id {id} not found")
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"User with id {id} deleted successfully ")
    
#Actualzar Usuario
@cli.command()
@click.argument('id',type=int)   
@click.option('--name',help='Name of the user')
@click.option('--lastname',help='Lastname of the user')
def update_user (id,name,lastname):
    data = json_manager.read_json()
    for user in data :
        if user['id']== id:
            if name is not None:
                user['name'] = name
            if lastname is not None:
                user['lastname'] = lastname
            break
    json_manager.write_json(data)
    print(f"User with id {id} update successfully ")
     

    

if __name__ == '__main__':
    cli()
