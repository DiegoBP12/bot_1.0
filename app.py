import web
import application.controllers.bot as bot

urls=('/home', 'application.controllers.principal.home.Home',
    '/index_batman','application.controllers.batman.index.Index',
    '/insert_batman', 'application.controllers.batman.insert.Insert',
    '/update_batman/(.*)', 'application.controllers.batman.update.Update',
    '/delete_batman/(.*)', 'application.controllers.batman.delete.Delete',
    '/view_batman/(.*)', 'application.controllers.batman.view.View',
    '/index_robin','application.controllers.robin.index.Index',
    '/insert_robin', 'application.controllers.robin.insert.Insert',
    '/update_robin/(.*)', 'application.controllers.robin.update.Update',
    '/delete_robin/(.*)', 'application.controllers.robin.delete.Delete',
    '/view_robin/(.*)', 'application.controllers.robin.view.View',
    '/index_villanos','application.controllers.robin.index.Index',
    '/insert_villanos', 'application.controllers.robin.insert.Insert',
    '/update_villanos/(.*)', 'application.controllers.robin.update.Update',
    '/delete_villanos/(.*)', 'application.controllers.robin.delete.Delete',
    '/view_vilanos/(.*)', 'application.controllers.robin.view.View')  #(url , ubicacion del archivo)

app = web.application(urls, globals())
render = web.template.render('application/views/clientes/', base = 'master2')

def run():
    bot.main()
    app.run()

if __name__ == "__main__": #metodo principal, doble guion = private
    web.config.debug = False # Hide debug print
    def NotFound():
        return web.notfound(render.notfound())
    app.notfound = NotFound
    def internalerror():
        return web.internalerror(render.internal())
    app.internalerror = internalerror
    run()
