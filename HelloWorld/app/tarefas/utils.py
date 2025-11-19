from app.models import Status

def popular_status_form(form):
    """Busca os status no BD e os adiciona como 'choices' no form."""
    
    # Esta linha faz uma chamada à base de dados
    status_choices = [(s.id, s.nome) for s in Status.query.order_by('nome').all()]
    
    print(f"Populando 'form.status.choices' com: {status_choices}")
    form.status.choices = status_choices