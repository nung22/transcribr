from flask_app import app, render_template, request, redirect, bcrypt, session, flash
from flask_app.models.recipe import Recipe

# Display recipe dashboard
@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('recipes.html', user_name = session['first_name'], all_recipes = Recipe.get_all(), user_id = session['user_id'])

# Display information for an individual recipe
@app.route('/recipes/<int:id>')
def recipes_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = { 'id' : int(id) }
    print(Recipe.get_by_id(data))
    return render_template('recipes_show.html', user_name = session['first_name'], recipe = Recipe.get_by_id(data))

# Display form to create new recipe
@app.route('/recipes/new')
def recipes_new():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('recipes_new.html', user_id = session['user_id'])

# Create new recipe and redirect to recipe dashbaord
@app.route('/new_recipe',methods=['POST'])
def new_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    Recipe.save(request.form)
    return redirect('/recipes')

# Display form to edit an existing recipe
@app.route('/recipes/<int:id>/edit')
def recipes_edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = { 'id' : id }
    return render_template('recipes_edit.html', recipe = Recipe.get_by_id(data))

# Edit an existing recipe and redirect to recipe dashboard
@app.route('/edit_recipe', methods=['POST'])
def edit():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        recipe_id = request.form['id']
        return redirect(f'/recipes/{recipe_id}/edit')
    Recipe.edit(request.form)
    return redirect('/recipes')

# Delete a recipe given its id
@app.route('/recipes/<int:id>/destroy')
def delete(id):
    data = { 'id' : id }
    Recipe.delete(data)
    return redirect('/recipes')