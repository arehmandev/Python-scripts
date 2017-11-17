#!/usr/bin/env python
# -*- coding: utf-8 -*-

# <bitbar.title>Kubeconfig Context and Namespace Changer</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Abdul Rehman</bitbar.author>
# <bitbar.author.github>copland</bitbar.author.github>
# <bitbar.desc>Displays active kubeconfig context, namespace and user and allows you to easily change contexts and namespaces.</bitbar.desc>
# <bitbar.dependencies>python,kubectl</bitbar.dependencies>

import yaml
import os

HOME_DIR = os.environ['HOME']
KUBECTL_PATH = ('/usr/local/bin/kubectl')
NAMESPACES = ["cw-autosit", "iddcsdpfeat1", "manualsit1", "manualsit2"]
NOW_NAMESPACE = ""
NOW_USER = ""


def current_context():
    with open(HOME_DIR + "/.kube/config", 'r') as stream:
        try:
            kube_data = yaml.load(stream)
            current_context = kube_data['current-context']
            return(current_context)

        except yaml.YAMLError as exc:
            print(exc)


def list_contexts():
    with open(HOME_DIR + "/.kube/config", 'r') as stream:
        try:
            print("CONTEXTS -----")
            kube_data = yaml.load(stream)
            allcontexts = kube_data['contexts']

            for i in range(len(allcontexts)):
                context = allcontexts[i]['name']
                print(context + " | bash=" + KUBECTL_PATH +
                      " param1=config param2=use-context param3=" + context + " terminal=false color=blue refresh=true")

        except yaml.YAMLError as exc:
            print(exc)


def list_namespaces(namespaces, context):
    print("NAMESPACES -----")
    for i in range(len(namespaces)):
        print(namespaces[i] + " | bash=" + KUBECTL_PATH +
              " param1=config param2=set-context param3=" + context + " param4=--namespace=" + namespaces[i] + " terminal=false color=purple refresh=true")


def get_namespace():
    with open(HOME_DIR + "/.kube/config", 'r') as stream:

        try:
            kube_data = yaml.load(stream)
            allcontexts = kube_data['contexts']
            for i in range(len(allcontexts)):
                context = allcontexts[i]['name']
                if current_context() in context:
                    return allcontexts[i]['context']['namespace']

        except yaml.YAMLError as exc:
            print(exc)


def get_user():
    with open(HOME_DIR + "/.kube/config", 'r') as stream:

        try:
            kube_data = yaml.load(stream)
            allcontexts = kube_data['contexts']
            for i in range(len(allcontexts)):
                context = allcontexts[i]['name']
                if current_context() in context:
                    return allcontexts[i]['context']['user']

        except yaml.YAMLError as exc:
            print(exc)


# Try find values else default to unset
try:
    NOW_NAMESPACE = get_namespace()
    NOW_USER = get_user()
except:
    NOW_NAMESPACE = "unset"
    NOW_USER = "unset"

print("K8S: " + current_context() + "/" + " | color=orange")
print('---')


print("Namespace: " + NOW_NAMESPACE)
print("User: " + NOW_USER)
print('---')
list_namespaces(NAMESPACES, current_context())
list_contexts()

