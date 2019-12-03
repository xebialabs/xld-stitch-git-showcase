def stitch(ctx, source):
    source.at("/metadata/labels").put("environment", "Some random env")
    source.at("/metadata/labels").put("version", "Some random app")
    return source
