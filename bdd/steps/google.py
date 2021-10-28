from behave import given, when, then

@given(u'Acesso a pagina do Google')
def step_impl(context):
    context.web.get('https://www.google.com.br/')

@when(u'Realizo uma pesquisa')
def step_impl(context):
    context.element = context.web.find_element_by_name('q')
    context.element.click()
    context.element.send_keys('Eduzz')
    context.element.submit()

@then(u'procurar o texto Vem crescer com a gente')
def step_impl(context):
    assert context.web.find_element_by_partial_link_text('Vem crescer com a gente')
